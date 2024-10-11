package com.devia;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

import com.datastax.oss.driver.api.core.CqlIdentifier;
import com.datastax.oss.driver.api.core.CqlSession;
import com.datastax.oss.driver.api.core.PagingIterable;
import com.datastax.oss.driver.api.core.cql.*;


public class App 
{
    public static void main( String[] args )
    {
        String keyspace = "translations";
        try (CqlSession session = CqlSession.builder().withKeyspace(CqlIdentifier.fromCql(keyspace)).build()) { 
            ResultSet rs = session.execute("select * from pl_fr");  
            List<Translation> translations =new ArrayList<Translation>();
            PagingIterable<Translation> pi = rs.map(result -> mapTranslation(result)) ; 
            System.out.println(pi.one().getSrc_text()) ;
        }
    }
    private static Translation mapTranslation(Row row) {

        
        Translation translation = new Translation() ; 

        translation.setSrc_lang(row.getString("src_lang"));
        translation.setSrc_text(row.getString("src_text"));
        translation.setTarget_lang(row.getString("target_lang"));
        translation.setTarget_text(row.getString("target_text"));

        return translation ;
    }
}
