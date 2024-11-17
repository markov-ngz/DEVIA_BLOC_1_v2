package com.devia.api.controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.security.access.prepost.PreAuthorize;

@RestController
public class MainController {

    @GetMapping("/")
    public String home() {
        return "Selamat ";
    }

    @GetMapping("/user/profile")
    @PreAuthorize("hasAnyAuthority('SCOPE_ROLE_USER','SCOPE_ROLE_ADMIN')") // Accessible par ROLE_USER et ROLE_ADMIN
    public String profile() {
        return "User here";
    }

    @GetMapping("/admin/profile")
    @PreAuthorize("hasAnyAuthority('SCOPE_ROLE_ADMIN')") // Accessible par ROLE_USER et ROLE_ADMIN
    public String adminProducts() {
        return "Admin here";
    }

}
