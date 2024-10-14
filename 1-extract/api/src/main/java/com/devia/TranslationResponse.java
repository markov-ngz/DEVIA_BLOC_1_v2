package com.devia;

/*
 * Translation to be returned by the HuggingFace API 
 */
public class TranslationResponse {
        private String translation_text ;

        public void setTranslation_text(String text){
            this.translation_text  = text ; 
        } 
        public String getTranslation_text(){
            return this.translation_text ; 
        }
}
