package com.devia;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringDeserializer;
import org.apache.kafka.common.serialization.StringSerializer;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.time.Duration;
import java.util.Collections;
import java.util.Properties;
import java.util.concurrent.Future;

public class KafkaHandler {
    private Properties producerProps;
    private Properties consumerProps;
    private KafkaProducer<String, String> producer;
    private KafkaConsumer<String, String> consumer;
    private final ObjectMapper objectMapper;

    public KafkaHandler() {
        this.objectMapper = new ObjectMapper();
    }

    public void setProperties(String bootstrapServers, String groupId) {
        // Producer properties
        producerProps = new Properties();
        producerProps.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        producerProps.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        producerProps.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class.getName());
        producerProps.put(ProducerConfig.ACKS_CONFIG, "all");
        producerProps.put(ProducerConfig.RETRIES_CONFIG, 3);

        // Consumer properties
        consumerProps = new Properties();
        consumerProps.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, bootstrapServers);
        consumerProps.put(ConsumerConfig.GROUP_ID_CONFIG, groupId);
        consumerProps.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        consumerProps.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, StringDeserializer.class.getName());
        consumerProps.put(ConsumerConfig.AUTO_OFFSET_RESET_CONFIG, "earliest");
        consumerProps.put(ConsumerConfig.ENABLE_AUTO_COMMIT_CONFIG, false);

        // Initialize producer and consumer
        producer = new KafkaProducer<>(producerProps);
        consumer = new KafkaConsumer<>(consumerProps);
    }

    public Future<?> publish(String topic, String key, String message) {
        try {
            ProducerRecord<String, String> record = new ProducerRecord<>(topic, key, message);
            return producer.send(record);
        } catch (Exception e) {
            throw new RuntimeException("Error publishing message to Kafka", e);
        }
    }

    public <T> Future<?> publish(String topic, String key, T object) {
        try {
            String jsonMessage = objectMapper.writeValueAsString(object);
            return publish(topic, key, jsonMessage);
        } catch (Exception e) {
            throw new RuntimeException("Error serializing object to JSON", e);
        }
    }

    public ConsumerRecords<String, String> consume(String topic, Duration timeout) {
        try {
            consumer.subscribe(Collections.singletonList(topic));
            return consumer.poll(timeout);
        } catch (Exception e) {
            throw new RuntimeException("Error consuming messages from Kafka", e);
        }
    }

    public <T> T parseJson(String jsonMessage, Class<T> clazz) {
        try {
            return objectMapper.readValue(jsonMessage, clazz);
        } catch (Exception e) {
            throw new RuntimeException("Error parsing JSON message", e);
        }
    }

    public <T> T parseJson(ConsumerRecord<String, String> record, Class<T> clazz) {
        return parseJson(record.value(), clazz);
    }

    public void close() {
        if (producer != null) {
            producer.close();
        }
        if (consumer != null) {
            consumer.close();
        }
    }
}