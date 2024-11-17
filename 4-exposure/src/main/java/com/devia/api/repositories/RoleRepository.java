package com.devia.api.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.devia.api.entities.Role;

@Repository
public interface RoleRepository extends JpaRepository<Role, String> {

}
