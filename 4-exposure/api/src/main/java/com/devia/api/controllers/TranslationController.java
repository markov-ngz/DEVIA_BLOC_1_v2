package com.devia.api.controllers;

import java.util.List;

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


import com.devia.api.entities.Translation;
import com.devia.api.repositories.TranslationRepository;

@RestController
@RequestMapping("/translation")
public class TranslationController {

    private final TranslationRepository translationRepository;

    public TranslationController(TranslationRepository repository) {
        this.translationRepository = repository;
    } 

    @GetMapping("")
    @PreAuthorize("hasAnyAuthority('SCOPE_ROLE_USER','SCOPE_ROLE_ADMIN')") // Accessible par ROLE_USER et ROLE_ADMIN
    public List<Translation> getAll() {
        return this.translationRepository.findAll();
    }
}
