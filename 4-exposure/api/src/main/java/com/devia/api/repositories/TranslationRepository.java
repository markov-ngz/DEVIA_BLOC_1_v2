package com.devia.api.repositories;

import com.devia.api.entities.Translation;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TranslationRepository extends JpaRepository<Translation, String> {

}
