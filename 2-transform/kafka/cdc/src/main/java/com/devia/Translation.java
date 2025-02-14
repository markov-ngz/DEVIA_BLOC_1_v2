package com.devia;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Translation {
    private String text_source  ; 

    private String text_target ; 

    private String lang_source = "french" ; 

    private String lang_target = "polish" ; 

    private Long ts_ms ; 

    private String source_type ;

    private String source_value ; 

    private final ObjectMapper objectMapper;

    public Translation(String text_source, String text_target, Long ts_ms, String source_value){
        
        this.text_source = text_source ; 
        this.text_target = text_target ; 
        this.ts_ms = ts_ms ; 
        this.source_type = "database" ; 
        this.source_value = source_value ; 

        this.objectMapper = new ObjectMapper();

    }

    public Long getTs_ms(){
        return this.ts_ms ; 
    }
    public String getSource_type(){
        return this.source_type ; 
    }

    public String getSource_value(){
        return this.source_value ; 
    }

    public String getText_source(){
        return this.text_source ; 
    }
    public String getText_target(){
        return this.text_target ; 
    }
    public String getLang_target(){
        return this.lang_target ; 
    }
    public String getLang_source(){
        return this.lang_source ; 
    }
    
    public String to_json() throws JsonProcessingException {
        
        return this.objectMapper.writerWithDefaultPrettyPrinter().writeValueAsString(this);
 
    }
}

