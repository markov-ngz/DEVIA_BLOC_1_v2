package com.devia.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.context.annotation.Bean;

import java.util.Set;

import org.springframework.boot.CommandLineRunner;

import com.devia.api.entities.Role;
import com.devia.api.entities.User;
import com.devia.api.repositories.RoleRepository;
import com.devia.api.repositories.UserRepository;

@SpringBootApplication
public class ApiApplication {

	public static void main(String[] args) {
		System.setProperty("spring.profiles.active", "dev");
		SpringApplication.run(ApiApplication.class, args);
	}

}
