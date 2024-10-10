package com.saksham.backend.controller;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.saksham.backend.entities.Admin;
import com.saksham.backend.entities.User;
import com.saksham.backend.services.AdminService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.Map;

@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api/v1/admin")

public class AdminController {

    @Autowired
    AdminService adminService;
    @PostMapping("/register")
    private ResponseEntity<String> registerUser(@RequestBody Admin admin) throws JsonProcessingException {
        if (adminService.findByEmail(admin.getEmail()) != null) {
            // Email already exists, handle the case (e.g., inform user)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("email already exist");
        }

        adminService.registerAdmin(admin);

        Admin loggedInAdmin = adminService.findByEmail(admin.getEmail());
        Map<String, String> response = new HashMap<>();
        response.put("message", "Login successful");
        response.put("adminId", loggedInAdmin.get_Id());


        ObjectMapper mapper = new ObjectMapper();
        String responseJson = mapper.writeValueAsString(response);

        return ResponseEntity.ok(responseJson);


    }

    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestBody Admin admin) throws JsonProcessingException {

        if (adminService.authenticateAdmin(admin.getEmail(), admin.getPassword())) {
            Admin loggedInAdmin = adminService.findByEmail(admin.getEmail());
            Map<String, String> response = new HashMap<>();
            response.put("message", "Login successful");
            response.put("adminId", loggedInAdmin.get_Id());


            ObjectMapper mapper = new ObjectMapper();
            String responseJson = mapper.writeValueAsString(response);

            return ResponseEntity.ok(responseJson);
        } else {
            // Invalid credentials
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("Invalid email or password");
        }
    }


}
