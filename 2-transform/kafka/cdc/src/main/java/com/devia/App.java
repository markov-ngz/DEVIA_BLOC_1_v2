package com.devia;

import com.devia.KafkaHandler;
/**
 * Hello world!
 */
public class App {
    public static void main(String[] args) {
        KafkaHandler kafka  = new KafkaHandler(); 

        kafka.setConsumer("mytopic","localhost:9092");

        kafka.readMessage();
    }
}
