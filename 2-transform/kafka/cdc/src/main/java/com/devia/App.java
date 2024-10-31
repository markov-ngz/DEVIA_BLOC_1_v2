package com.devia;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.time.Duration;
import java.util.concurrent.Future;

import org.apache.kafka.clients.admin.AdminClient;
import org.apache.kafka.clients.admin.AdminClientConfig;
import org.apache.kafka.clients.admin.CreateTopicsResult;
import org.apache.kafka.clients.admin.DescribeClusterResult;
import org.apache.kafka.clients.admin.NewTopic;
import org.apache.kafka.common.KafkaFuture;
import org.apache.kafka.common.internals.Topic;

import java.util.Collection;
import java.util.Collections;
import java.util.Properties;

/**
 * Hello world!
 */
public class App {

    private static final Logger Logger = LogManager.getLogger(App.class);

    public static void main(String[] args) throws Exception{

        // 0. Setup 
        KafkaHandler handler = new KafkaHandler() ; 
        handler.setProperties("127.0.0.1:9092", "mygroup");
        String debezium_topic = "connector.public.translations"  ; 
        String target_topic  = "translations.raw.frpl" ;

        // 1. Get records from Topic 
        ConsumerRecords<String, String> records = handler.consume(debezium_topic, Duration.ofSeconds(10));

        // 2. Format the read records to the one expected
        for (ConsumerRecord<String, String> record : records) {
            try {
                // 2.1 Deserialiase Json Record
                DebeziumMessage obj = handler.parseJson(record, DebeziumMessage.class);

                // 2.2 Get the value of the new data inserted 
                TranslationValue value = obj.getPayload().getAfter();

                Logger.info(value.getFrench());

                // 2.3 Map it to the expected the format
                Translation final_translation = new Translation(value.getFrench(), value.getPolish()) ;

                // 2.4 Publish the serialized object to a topic 
                handler.publish(target_topic, "key2", final_translation).get();
                
                Logger.info(final_translation.to_json());

            } catch (Exception e) {
                Logger.error(e);
                throw e ;
            } 
        }
        handler.close();
    }
}
