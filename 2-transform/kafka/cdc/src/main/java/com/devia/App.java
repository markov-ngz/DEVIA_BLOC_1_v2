package com.devia;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.time.Duration;
import java.util.concurrent.Future;
/**
 * Hello world!
 */
public class App {

    private static final Logger Logger = LogManager.getLogger(App.class);

    public static void main(String[] args) throws Exception{
        
    System.setProperty("log4j.configurationFile","./log4j2.xml");

    /// 0. Configuration
    String topic_name = "connector.public.translations"; 

    KafkaHandler handler = new KafkaHandler();

    handler.setProperties("localhost:9092", "example");

    // handler.publish("translations.frpl", "key2", "does not seem to work").get() ; 

    ConsumerRecords<String, String> records = handler.consume("translations.frpl", Duration.ofSeconds(10));
    for (ConsumerRecord<String, String> record : records) {
        System.out.println("Record :");
        System.out.println(record);
    }

    // // 1. Get records from Topic 
    // ConsumerRecords<String, String> records = handler.consume(topic_name, Duration.ofSeconds(10));

    // // 2. Format the read records to the one expected
    // for (ConsumerRecord<String, String> record : records) {
    //     try {
    //         // 2.1 Deserialiase Json Record
    //         DebeziumMessage obj = handler.parseJson(record, DebeziumMessage.class);

    //         // 2.2 Get the value of the new data inserted 
    //         TranslationValue value = obj.getPayload().getAfter();


    //         // 2.3 Map it to the expected the format
    //         Translation final_translation = new Translation(value.getFrench(), value.getPolish()) ;

    //         // 2.4 Publish the serialized object to a topic 
    //         handler.publish("translations.frpl", "key2", final_translation);
            
    //         Logger.info(final_translation.to_json());

    //     } catch (Exception e) {
    //         Logger.error(e);
    //         throw e ;
    //     }
    // }
    
    handler.close();

    }


}
