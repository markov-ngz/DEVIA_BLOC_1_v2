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
    ConsumerRecords<String, String> records = handler.consume("my-topic", Duration.ofMillis(100));
    for (ConsumerRecord<String, String> record : records) {
        System.out.println(record);
        DebeziumMessage obj = handler.parseJson(record, DebeziumMessage.class);
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
