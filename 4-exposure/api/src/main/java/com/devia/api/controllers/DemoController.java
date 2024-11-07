package com.devia.api.controllers;

import java.util.List;

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.devia.api.entities.DemoEntity;
import com.devia.api.repositories.DemoRepository;

@RestController
@RequestMapping("api/demo")
public class DemoController {

    private final DemoRepository demoRepository;

    public DemoController(DemoRepository demoRepository) {
        this.demoRepository = demoRepository;
    }
    
    @GetMapping("/user")
    @PreAuthorize("hasAuthority('SCOPE_ROLE_USER')")
    public String userAccess() {
        return "User access";
    }

    @GetMapping("/admin")
    @PreAuthorize("hasAuthority('SCOPE_ROLE_ADMIN')")
    public String adminAccess() {
        return "Admin access";
    }


    @GetMapping("")
    @PreAuthorize("hasAnyAuthority('SCOPE_ROLE_USER','SCOPE_ROLE_ADMIN')") // Accessible par ROLE_USER et ROLE_ADMIN
    public List<DemoEntity> getAll() {
        return this.demoRepository.findAll();
    }

    @PostMapping("")
    @PreAuthorize("hasAnyAuthority('SCOPE_ROLE_ADMIN')") // Accessible par ROLE_USER et ROLE_ADMIN
    public DemoEntity createDemo(@RequestBody DemoEntity entity) {
        return this.demoRepository.save(entity);
    }

}
