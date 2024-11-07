package com.devia.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.context.annotation.Bean;

import java.util.Set;

import org.springframework.boot.CommandLineRunner;

import com.devia.api.entities.DemoEntity;
import com.devia.api.entities.Role;
import com.devia.api.entities.User;
import com.devia.api.repositories.DemoRepository;
import com.devia.api.repositories.RoleRepository;
import com.devia.api.repositories.UserRepository;

@SpringBootApplication
public class ApiApplication {

	public static void main(String[] args) {
		System.setProperty("spring.profiles.active", "dev");
		SpringApplication.run(ApiApplication.class, args);
	}

	@Bean
	CommandLineRunner commandLineRunner(DemoRepository demoRepository, UserRepository userRepository,
			RoleRepository roleRepository, PasswordEncoder passwordEncoder) {
		return args -> {
			demoRepository.save(new DemoEntity("Tacos"));

			// manually creates roles and users on startup
			Role roleUser = new Role();
			roleUser.setName("ROLE_USER");
			roleUser = roleRepository.save(roleUser);
			Role roleAdmin = new Role();
			roleAdmin.setName("ROLE_ADMIN");
			roleAdmin = roleRepository.save(roleAdmin);

			User admin = new User();
			admin.setUsername("admin@example.com");
			admin.setPassword(passwordEncoder.encode("securepassword"));
			admin.setRoles(Set.of(roleAdmin));
			userRepository.save(admin);

			User user = new User();
			user.setUsername("john@example.com");
			user.setPassword(passwordEncoder.encode("snow"));
			user.setRoles(Set.of(roleUser));
			userRepository.save(user);
		};
	}


}
