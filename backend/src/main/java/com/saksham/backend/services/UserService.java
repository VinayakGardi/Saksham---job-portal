package com.saksham.backend.services;

import com.saksham.backend.entities.User;
import com.saksham.backend.repo.UserRepository;
import org.python.google.common.base.Optional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    public User registerUser(User user){
        return userRepository.save(user);
    }

    public boolean authenticateUser(String email, String password) {
        User user = userRepository.findByEmail(email);
        if (user != null && password != null && password.equals(user.getPassword())) {
            return true; // Successful login
        } else {
            return false; // Invalid credentials
        }
    }

    public User findByEmail(String email) {
        return userRepository.findByEmail(email);
    }




    }

