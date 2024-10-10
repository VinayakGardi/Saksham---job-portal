package com.saksham.backend.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.saksham.backend.services.FileService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@RestController
@CrossOrigin(origins = "*")
@RequestMapping("/api/v1/file")
public class FileController {
    @Autowired
    private FileService fileService;

    @PostMapping("/upload")
    public ResponseEntity<?> upload(@RequestParam("file")MultipartFile file) throws IOException {

        String fileId  = fileService.addFile(file);
        Map<String, String> response = new HashMap<>();
        response.put("file_id", fileId);

        ObjectMapper mapper = new ObjectMapper();
        String responseJson = mapper.writeValueAsString(response);

        return ResponseEntity.ok(responseJson);
    }
}
// sample comment
