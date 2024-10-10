package com.saksham.backend.repo;

import com.saksham.backend.entities.Admin;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AdminRepository extends CrudRepository<Admin, String> {
    Admin findByEmail(String email);
}
