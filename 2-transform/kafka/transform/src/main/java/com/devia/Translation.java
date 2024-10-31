package com.devia;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Translation {
    private String text_source  ; 

    private String text_target ; 

    private String lang_source  ; 

    private String lang_target ; 

    private Long ts_ms ; 

    public Long getTs_ms(){
        return this.ts_ms ; 
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

    public void setTs_ms(Long ts_ms){
        this.ts_ms = ts_ms ; 
    }

    public void setText_source(String text_source){
        this.text_source = text_source ; 
    }
    public void setText_target(String text_target){
        this.text_target = text_target ; 
    }
    public void setLang_target(String lang_target){
        this.lang_target = lang_target; 
    }
    public void setLang_source(String lang_source){
        this.lang_source  = lang_source; 
    }
}

