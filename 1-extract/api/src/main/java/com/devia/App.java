package com.devia;

import com.devia.IngestionProducer;
import com.fasterxml.jackson.databind.ObjectMapper;
/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) throws Exception {
        String bootstrap_server = System.getenv("KAFKA_BOOTSTRAP_SERVER"); ; 
        String publish_topic = System.getenv("KAFKA_TOPIC"); ; 
        // IngestionProducer producer = new IngestionProducer(publish_topic,bootstrap_server);
        
        ObjectMapper objectMapper = new ObjectMapper();

        TranslationPayload map = new TranslationPayload("Bonjour");
        String requestBody = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(map);
        System.out.println(requestBody);
    
    }
}
