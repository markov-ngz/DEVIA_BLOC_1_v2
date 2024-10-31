package com.devia;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.time.Duration;

/**
 * Hello world!
 */
public class App {

    private static final Logger Logger = LogManager.getLogger(App.class);

    public static void main(String[] args) throws Exception{
        
        System.setProperty("log4j.configurationFile","./log4j2.xml");
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

                DebeziumSource source  = obj.getPayload().getSource() ; 
                
                String source_value = source.getDb() + "." + source.getSchema() + "." + source.getTable()  ;

                // 2.3 Map it to the expected the format
                Translation final_translation = new Translation(
                                                    value.getFrench(), 
                                                    value.getPolish(), 
                                                    obj.getPayload().getTsMs(),
                                                    source_value) ;

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
