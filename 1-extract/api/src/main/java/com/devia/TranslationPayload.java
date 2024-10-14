package com.devia;

import java.util.HashMap;
import java.util.Map;

import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.databind.ser.std.MapSerializer;

/*
 * Translation payload to send to the HuggingFace API 
 */
public class TranslationPayload {
    
    private String inputs ; 

    private HashMap<String,String> parameters = new HashMap<>();

    public TranslationPayload(String sentence) {
        this.inputs = sentence ; 
        this.parameters.put("src_lang", "fr_XX");
        this.parameters.put("tgt_lang", "pl_PL");
    }
    public String getInputs(){
        return this.inputs ; 
    }
    public Map<String,String> getParameters(){
        return this.parameters;
    }
    public void setInputs(String inputs){
        this.inputs = inputs ; 
    }
}
