package com.devia.api.entities;

import jakarta.persistence.Table;
import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import org.hibernate.annotations.Immutable ; 
import jakarta.persistence.GenerationType;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;

@Entity
@Immutable
@Table(name="translation_view")
public class Translation {
    public Translation(){}

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(name = "lang_origin")
    private String lang_origin;

    @Column(name = "lang_target")
    private String lang_target;

    @Column(name = "text_origin")
    private String text_origin  ; 

    @Column(name = "text_target")
    private String text_target ; 

    @Column(name = "source_name")
    private String source_name ; 

    @Column(name = "source_type")
    private String source_type ; 

    @Column(name = "extracted_at")
    private String extractedAt ; 


    public String getSource_type(){
        return this.source_type ; 
    }

    public String getSource_name(){
        return this.source_name ; 
    }

    public String getExtractedAt(){
        return this.extractedAt ; 
    }

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

    @Override
    public String toString() {
        return "{" +
                " "+getLang_origin()+"='" + getText_origin() + "'" +
                ", "+getLang_origin()+"='" + getText_target() + "'" +
                "}";
    }
}
