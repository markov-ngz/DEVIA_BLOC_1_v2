package com.devia;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.Duration;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.apache.kafka.clients.consumer.ConsumerRecords;
import org.apache.kafka.common.protocol.types.Field.Str;

import com.devia.KafkaHandler;
import com.devia.PostgresHandler;
 
public class App {
    private static final Logger Logger = LogManager.getLogger(App.class);
    public static void main(String[] args) throws Exception {
        System.setProperty("log4j.configurationFile","./log4j2.xml");

        // 0. Setup handler
        KafkaHandler handler = new KafkaHandler() ;
        handler.setProperties("127.0.0.1:9092", "mygroup");
        String clean_topic  = "translations.clean.frpl" ;

        // 1. Read messages from topic 
        ConsumerRecords<String, String> records = handler.consume(clean_topic, Duration.ofSeconds(10));

        handler.close();

        // 2. Instnatiate datbase connection
        PostgresHandler pgHandler = getDatabaseHandler() ; 

        // 3. Insert the new data 
        insertCleanData(records, handler,pgHandler) ; 
        
        pgHandler.disconnect();

    }


    private static PostgresHandler getDatabaseHandler()throws SQLException{

        String url = "jdbc:postgresql://localhost:7432/TARGET_DB" ; 
        String user = "TARGET_USER" ; 
        String password = "raditz" ; 


        PostgresHandler pgHandler = new PostgresHandler(url, user, password) ; 

        pgHandler.connect();
        if (pgHandler.isConnected()){
            return pgHandler ; 
        }else{
            throw new SQLException("Unable to connect to database please check credentials ") ; 
        }
        
    }

    private static void insertCleanData(ConsumerRecords<String,String> records,KafkaHandler kafkaHandler,PostgresHandler DBhandler) throws Exception{
        
        String queryTranslation = "INSERT INTO public.translations(text_origin, text_target, extracted_at ,languages_id, source_id) VALUES ('%s','%s','%s',%s,%s) ON CONFLICT DO NOTHING ; " ; 
        

        for (ConsumerRecord<String, String> record : records) {
           
            
            CleanTranslation translation = kafkaHandler.parseJson(record, CleanTranslation.class) ; 
            
            Integer sourceId = getSourceId(translation, DBhandler) ;

            Integer languagesId =  getLanguagesId(translation, DBhandler) ; 

            if (sourceId == null || languagesId == null ){
                Logger.error("Could not fetch Source Id from existing or inserted row");
                continue ; 
            }else{
                String queryFormatted = String.format(queryTranslation,translation.getText_source(), translation.getText_target(), translation.getExtractedAt(),languagesId.toString(), sourceId.toString()) ; 
                
                System.out.println(queryFormatted) ; 
                ResultSet result = DBhandler.executeQuery(queryFormatted) ; 

            }

            break ;
        }
    }
    /*
     * Insert the source and retrieve the id 
     * If the source exists, retrieve its id 
     */
    private static Integer getSourceId(CleanTranslation translation , PostgresHandler DBhandler)throws SQLException{

        Integer sourceId = null ; 

        String querySource = "INSERT INTO public.source (type, name) VALUES ('%s','%s') ON CONFLICT DO NOTHING RETURNING id ;" ; 
        String querySourceId = "SELECT id FROM public.source WHERE type = '%s' AND name = '%s' ;" ; 

        String querySourceformatted = String.format(querySource, translation.getSource_type(), translation.getSource_value())  ; 
        ResultSet result = DBhandler.executeQuery(querySourceformatted) ; 
        Integer i = 0 ;

        while (result.next()) {
            i += 1 ;
            sourceId = result.getInt("id");
        }
        if (i == 0){
            
            String querySpecificSourceId = String.format(querySourceId,translation.getSource_type(), translation.getSource_value()) ; 
            ResultSet sourceIdSet =  DBhandler.executeQuery(querySpecificSourceId) ; 

            while (sourceIdSet.next()) {
                sourceId = sourceIdSet.getInt("id") ; 
            }
        }

        return sourceId ; 
    }

    private static Integer getLanguagesId(CleanTranslation translation , PostgresHandler DBhandler)throws SQLException {
        Integer languagesId = null ; 
        String queryLanguages = "INSERT INTO public.languages (lang_origin, lang_target) VALUES ('%s','%s') ON CONFLICT DO NOTHING RETURNING id ;" ; 
        String queryLanguagesId = "SELECT id FROM public.languages WHERE lang_origin ='%s' AND lang_target = '%s' ;" ; 

        String queryFormatted = String.format(queryLanguages, translation.getSource_type(), translation.getSource_value())  ; 
        ResultSet result = DBhandler.executeQuery(queryFormatted) ; 
        Integer i = 0 ;

        while (result.next()) {
            i += 1 ;
            languagesId = result.getInt("id");
        }
        if (i == 0){
            
            String querySpecificId = String.format(queryLanguagesId,translation.getSource_type(), translation.getSource_value()) ; 
            ResultSet sourceIdSet =  DBhandler.executeQuery(querySpecificId) ; 

            while (sourceIdSet.next()) {
                languagesId = sourceIdSet.getInt("id") ; 
            }
        }

        return languagesId ; 
    }
}
