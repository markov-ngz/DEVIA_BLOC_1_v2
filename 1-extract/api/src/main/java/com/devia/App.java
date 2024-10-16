package com.devia;

import java.net.http.HttpResponse;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.apache.kafka.shaded.com.google.protobuf.Api;

import com.devia.IngestionProducer;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) throws Exception {
        String bootstrap_server = System.getenv("KAFKA_BOOTSTRAP_SERVER"); ; 
        String publish_topic = System.getenv("KAFKA_TOPIC"); ; 

        // String url = "https://api-inference.huggingface.co/models/facebook/mbart-large-50-many-to-many-mmt" ; 
        // IngestionProducer producer = new IngestionProducer(publish_topic,bootstrap_server);
        
        ObjectMapper objectMapper = new ObjectMapper();

        TranslationPayload map = new TranslationPayload("Bonjour");
        // String requestBody = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(map);
        
        // ApiHandler api = new ApiHandler();
        // HttpResponse<String> response = api.sendPOST(url, requestBody);
        // System.out.println(response.body());
        String body = "[{\"translation_text\":\"Witaj!\"}]" ; 

        TranslationResponse[] translated_texts = objectMapper.readValue(body, TranslationResponse[].class);
        
        Translation final_translation = new Translation(map.getInputs(), translated_texts[0].getTranslation_text());

        String translation_json = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(final_translation);

        System.out.println(translation_json);

        // producer.writeMessage("123456", "random");

        // producer.producer.close();
    }
}
