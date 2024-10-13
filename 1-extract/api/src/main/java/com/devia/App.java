package com.devia;
import com.devia.IngestionProducer;
/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        String bootstrap_server = System.getenv("KAFKA_BOOTSTRAP_SERVER"); ; 
        String publish_topic = System.getenv("KAFKA_TOPIC"); ; 
        // IngestionProducer producer = new IngestionProducer(publish_topic,bootstrap_server);


    
    }
}
