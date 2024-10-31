package com.devia;

import java.time.Duration;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;

import com.devia.KafkaHandler;
import com.devia.Translation;
/**
 * Hello world!
 *
 */
public class App
{
    private static final Logger Logger = LogManager.getLogger(App.class);
    public static void main( String[] args ) throws Exception
    {
        System.setProperty("log4j.configurationFile","./log4j2.xml");

        // 0. Setup
        KafkaHandler handler = new KafkaHandler() ; 
        handler.setProperties("127.0.0.1:9092", "mygroup");
        String raw_topic = "translations.raw.frpl" ; 
        String clean_topic  = "translations.clean.frpl" ;

        ConsumerRecords<String, String> records = handler.consume(raw_topic, Duration.ofSeconds(10));

        for (ConsumerRecord<String, String> record : records) {
            Translation translation = handler.parseJson(record, Translation.class) ; 
            Logger.info(translation.getLang_source()) ; 
        }

        handler.close() ; 
    }
}
