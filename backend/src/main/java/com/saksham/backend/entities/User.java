package com.saksham.backend.entities;

import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;
import org.springframework.http.ResponseEntity;
import org.springframework.web.multipart.MultipartFile;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

@Document(collection = "Users")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class User {

    @Id
    private String _id ;
    private String name;
    private String email;
    private String password;
    private String phone_Number;
    private String location;
    private String experience;
    private String education;
    private String age;
    private String category;

    @JsonInclude(JsonInclude.Include.NON_NULL)
    private List<String> eligible_jobs = null;
    public String get_Id() {
        return _id;
    }


}