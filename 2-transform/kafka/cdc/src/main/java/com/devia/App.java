package com.devia;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.time.Duration;
/**
 * Hello world!
 */
public class App {

    private static final Logger Logger = LogManager.getLogger(App.class);
    public static void main(String[] args) throws Exception{

    System.setProperty("log4j.configurationFile","./log4j2.xml");

    

    TranslationValue value = new TranslationValue();
    value.setFrench("J'habite à Paris");
    value.setPolish("Mieszkam w Paris");

    Translation final_translation = new Translation(value.getFrench(), value.getPolish()) ;

    ObjectMapper objectMapper = new ObjectMapper();

    String translation_json = objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(final_translation);

    Logger.info(translation_json);
    // Initialize the handler
    // KafkaHandler handler = new KafkaHandler();
    // handler.setProperties("localhost:9092", "example");

    // // Consuming messages
    // String topic_name = "connector.public.translations"; 
    // ConsumerRecords<String, String> records = handler.consume(topic_name, Duration.ofSeconds(10));
    // for (ConsumerRecord<String, String> record : records) {

    //     try {
    //         DebeziumMessage obj = handler.parseJson(record, DebeziumMessage.class);
    //         System.out.println(obj.getPayload().getAfter().getFrench());
    //     } catch (Exception e) {
    //         Logger.error(e);
    //         handler.close();

    //     }

    // }

    // // // Publishing messages
    // // handler.publish("my-topic", "key1", "Hello World");

    // // // Publishing objects
    // // TranslationPayload myObject = new TranslationPayload();
    // // handler.publish("my-topic", "key2", myObject);
    // // Clean up
    // handler.close();
    }

}
