package com.devia;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;

import com.devia.KafkaHandler;
import java.time.Duration;
/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
    // Initialize the handler
    KafkaHandler handler = new KafkaHandler();
    handler.setProperties("localhost:9092", "my-group-id");

    // Consuming messages
    String topic_name = "connector.public.translation"; 
    ConsumerRecords<String, String> records = handler.consume(topic_name, Duration.ofMillis(100));
    for (ConsumerRecord<String, String> record : records) {
        System.out.println(record);
        DebeziumMessage obj = handler.parseJson(record, DebeziumMessage.class);
        System.out.println(obj.getPayload());
        // Process the object
    }

    // // Publishing messages
    // handler.publish("my-topic", "key1", "Hello World");

    // // Publishing objects
    // TranslationPayload myObject = new TranslationPayload();
    // handler.publish("my-topic", "key2", myObject);
    // Clean up
    handler.close();
    }
}
