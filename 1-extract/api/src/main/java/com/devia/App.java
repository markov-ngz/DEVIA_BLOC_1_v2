package com.devia;

import java.net.http.HttpResponse;
import java.util.concurrent.TimeUnit;

import com.fasterxml.jackson.databind.ObjectMapper;
/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) throws Exception {

        // Kafka Topic whereabouts 
        String bootstrap_server = System.getenv("KAFKA_BOOTSTRAP_SERVER"); 
        String publish_topic = System.getenv("KAFKA_TOPIC"); 

        // data that will be translated 
        String[] item_to_translate = {"Salut!","Cours !","Courez !","Qui ?","Ça alors !","Au feu !","À l'aide !","Saute.","Ça suffit !","Stop !"} ; 

        // API to call 
        String url = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt" ; 
        
        // Producer 
        IngestionProducer producer = new IngestionProducer(publish_topic,bootstrap_server);

        // Api handler 
        ApiHandler api = new ApiHandler();

        // OBject Mapper to de/serialize 
        ObjectMapper objectMapper = new ObjectMapper();

        // Iterate over the sentences 
        for (String sentence : item_to_translate) {

            TranslationPayload translation_payload = new TranslationPayload(sentence);

            String requestBody = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(translation_payload);
            
            
            HttpResponse<String> response = api.sendPOST(url, requestBody);

            String body = response.body() ; 

            TranslationResponse[] translated_texts = objectMapper.readValue(body, TranslationResponse[].class);
            
            Translation final_translation = new Translation(translation_payload.getInputs(), translated_texts[0].getTranslation_text());

            String translation_json = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(final_translation);

            // value is used as key in order to avoid duplicate to the topic 
            producer.writeMessage(translation_json, translation_json);
            
            // delay to avoid rate limit from API 
            TimeUnit.SECONDS.sleep(1);
        }

        producer.producer.close();
    }
}
