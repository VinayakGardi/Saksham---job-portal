package com.saksham.backend.entities;

import lombok.*;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "Admins")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class Admin {
    private String _id ;

    private String email;
    private String password;

    private String fileId;

    private int docParsed = 0;

    private String Summery;
    public String get_Id() {
        return _id;
    }
}
