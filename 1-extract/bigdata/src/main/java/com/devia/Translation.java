package com.devia;
import java.util.UUID;

import com.datastax.oss.driver.api.mapper.annotations.CqlName;
import com.datastax.oss.driver.api.mapper.annotations.Entity;
import com.datastax.oss.driver.api.mapper.annotations.PartitionKey;

@Entity
@CqlName("pl_fr")
public class Translation {

    @PartitionKey
    private String id ; 
    private String src_lang;
    private String target_lang; 
    private String src_text; 
    private String target_text; 

    public String getId() {
        return id;
    }
    public void setId(String id) {
        this.id = id;
    }
    public String getSrc_lang() {
        return src_lang;
    }
    public void setSrc_lang(String src_lang) {
        this.src_lang = src_lang;
    }
    public String getSrc_text() {
        return src_text;
    }
    public void setSrc_text(String src_text) {
        this.src_text = src_text;
    }

    public String getTarget_lang() {
        return target_lang;
    }
    public void setTarget_lang(String target_lang) {
        this.target_lang = target_lang;
    }
    public String getTarget_text() {
        return target_text;
    }
    public void setTarget_text(String target_text) {
        this.target_text = target_text;
    }
}
