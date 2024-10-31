package com.devia;


public class Translation {
    private String text_source  ; 

    private String text_target ; 

    private String lang_source = "fr" ; 

    private String lang_target = "pl" ; 

    private Long ts_ms ; 

    public Translation(String text_source, String text_target ){
        this.text_source = text_source ; 
        this.text_target = text_target ; 
        this.ts_ms = System.currentTimeMillis() % 1000;
    }

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
}
