package com.aryakadam.myapplication2_multiplicationtable;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;
import android.widget.Button;
import android.view.View;

public class MainActivity extends AppCompatActivity {
    private Button button;
    private TextView table;
    private TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        button = findViewById(R.id.button);
        table = findViewById(R.id.table);
        textView = findViewById(R.id.editTextNumber);

    }


    public void printTable(View view){
        int n = Integer.parseInt(textView.getText().toString());
        String t = "";
        for(int i=1;i<=10;i++){
            t+= n+" x "+i+" = "+n*i+"\n";
        }
        table.setText(t);
    }
}