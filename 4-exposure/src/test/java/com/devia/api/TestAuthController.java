package com.devia.api ;

import static org.hamcrest.Matchers.containsString;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import org.springframework.http.MediaType ;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.util.Set;

import org.junit.jupiter.api.Test;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

import com.devia.api.entities.Role;
import com.devia.api.entities.User;
import com.devia.api.repositories.UserRepository;
import com.fasterxml.jackson.databind.ObjectMapper;

/*
 * for status code : https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/test/web/servlet/result/StatusResultMatchers.html 
 */
@SpringBootTest
@AutoConfigureMockMvc
class TestAuthController {

	@Autowired
	private MockMvc mockMvc;

	@Test
	void registerSuccessfull() throws Exception {

        // Create a user object
        Role roleUser = new Role();
        roleUser.setName("ROLE_USER");
        
        User user = new User();
			user.setUsername("jojo@kudakenai.com");
			user.setPassword("unbreakble");
			user.setRoles(Set.of(roleUser));

        ObjectMapper objectMapper = new ObjectMapper();
        String json = objectMapper.writeValueAsString(user);
        System.out.println(json) ; 
		this.mockMvc.perform(
            post("/auth/register")
            .contentType(MediaType.APPLICATION_JSON)
            .content(json)
            .characterEncoding("utf-8"))
            .andExpect(status().isOk()
        ).andReturn() ; 
	}
}
