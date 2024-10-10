package com.saksham.backend.services;

import com.saksham.backend.entities.Admin;
import com.saksham.backend.repo.AdminRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AdminService {
    @Autowired
    private AdminRepository adminRepository;

    public Admin registerAdmin(Admin admin){
        return adminRepository.save(admin);
    }

    public boolean authenticateAdmin(String email, String password) {
        Admin admin = adminRepository.findByEmail(email);
        if (admin != null && password != null && password.equals(admin.getPassword())) {
            return true; // Successful login
        } else {
            return false; // Invalid credentials
        }
    }

    public Admin findByEmail(String email) {
        return adminRepository.findByEmail(email);
    }
}
