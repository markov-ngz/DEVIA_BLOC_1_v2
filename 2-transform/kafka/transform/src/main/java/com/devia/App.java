package com.devia;

import java.lang.reflect.Array;
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

        Integer count_publish = 0 ; 
        Integer count_errors = 0 ;

        ConsumerRecords<String, String> records = handler.consume(raw_topic, Duration.ofSeconds(10));

        for (ConsumerRecord<String, String> record : records) {
            
            Translation translation = handler.parseJson(record, Translation.class) ; 
            
            try {
                Translation cleanTranslation = transform(translation) ; 
                handler.publish(clean_topic, "key", cleanTranslation) ; 
                count_publish += 1 ; 
            } catch (Exception e) {
                count_errors += 1 ; 
                Logger.error(e.getMessage());
            }
   
        }
        Logger.info(String.format("Successfully published %s messages",count_publish.toString()));
        Logger.info(String.format("Failed to publish %s messages", count_errors.toString())) ; 
        handler.close() ; 
    }

    private static Translation transform(Translation translation) throws Exception {

        // 1. Extract text value fields 
        String text_source = translation.getText_source() ; 
        String text_target = translation.getText_target() ;
        
        // 2. Clean for 
        String clean_text_source = clean(text_source);
        String clean_text_target = clean(text_target) ; 

        translation.setText_source(clean_text_source);
        translation.setText_target(clean_text_target);

        return translation ; 

    }

    private static String clean(String text)throws IllegalArgumentException{
        Integer length = text.length() ; 
        // Rule 1 : Minimum length 
        if ( length < 3 ){
            String message = String.format("Text Length must not be under 3. Got %s for text %s",length.toString(), text) ; 
            throw new IllegalArgumentException(message) ; 
        }
        // Rule 2 : No characters like  / ( ) { }
        String[] forbidden_characters = {"//","(",")","{","}"} ;
        String replacement = " " ;
        for(String character : forbidden_characters){
            text = text.replace(character,replacement ) ;
        } 

        return text ; 
    }
}
