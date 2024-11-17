package com.devia.api.controllers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.stream.Collectors;

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.devia.api.dto.TranslationDTO;
import com.devia.api.entities.Translation;
import com.devia.api.repositories.TranslationRepository;

@RestController
@RequestMapping("/translation")
public class TranslationController {

    private final TranslationRepository translationRepository;

    // private Mapper mapper ; 

    public TranslationController(TranslationRepository repository) {
        this.translationRepository = repository;
    } 

    @GetMapping("")
    @PreAuthorize("hasAnyAuthority('SCOPE_ROLE_USER','SCOPE_ROLE_ADMIN')") // Accessible par ROLE_USER et ROLE_ADMIN
    public List<Map<String,String>> getAll() {
        // List<Translation> -> Stream -> (TranslationDTO -> Map<String,String>) -> List<Map<String,String>>
        return translationRepository.findAll().stream().map((obj) -> new TranslationDTO(
                obj.getText_origin(), 
                obj.getText_target(), 
                obj.getLang_origin(), 
                obj.getLang_target()).toJSON())
            .collect(Collectors.toList());
    }
}
