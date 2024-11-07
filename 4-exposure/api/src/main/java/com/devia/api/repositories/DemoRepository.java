package com.devia.api.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.devia.api.entities.DemoEntity;

@Repository
public interface DemoRepository extends JpaRepository<DemoEntity, String> {

}
