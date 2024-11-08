package com.devia.api;

import static org.hamcrest.Matchers.containsString;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultHandlers.print;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import org.junit.jupiter.api.Test;

import org.springframework.security.test.context.support.WithMockUser;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

/*
 * for status code : https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/test/web/servlet/result/StatusResultMatchers.html 
 * 
 */
@SpringBootTest
@AutoConfigureMockMvc
class TestMainController {

	@Autowired
	private MockMvc mockMvc;

	@Test
	void shouldBeUnauthorized() throws Exception {
		this.mockMvc.perform(get("/")).andDo(print()).andExpect(status().isUnauthorized());
	}

	@Test
	@WithMockUser
	void shouldReturnDefaultMessage() throws Exception {
		this.mockMvc.perform(get("/")).andDo(print()).andExpect(status().isOk());
	}
}