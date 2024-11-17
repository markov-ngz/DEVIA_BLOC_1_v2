package com.devia.api.dto;

public class TranslationDTO {

    private String lang_origin;
 
    private String lang_target;

    private String text_origin  ; 

    private String text_target ; 


    public String getText_origin(){
        return this.text_origin ; 
    }
    public String getText_target(){
        return this.text_target ; 
    }
    public String getLang_target(){
        return this.lang_target ; 
    }
    public String getLang_origin(){
        return this.lang_origin ; 
    }

    public void setText_origin(String text_origin){
        this.text_origin  = text_origin; 
    }
    public void setText_target(String text_target){
        this.text_target = text_target ; 
    }
    public void setLang_target(String lang_target){
        this.lang_target = lang_target ; 
    }
    public void setLang_origin(String lang_origin){
        this.lang_origin  = lang_origin; 
    }

    public TranslationDTO(String text_origin, String text_target, String lang_target, String lang_origin ){
        this.text_origin = text_origin ; 
        this.text_target = text_target ; 
        this.lang_target = lang_target ; 
        this.lang_origin  = lang_origin; 
    }
}
