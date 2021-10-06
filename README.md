# Medical Insurance Premium Prediction

## Final project : หลักสูตรบัณฑิตพันธ์ใหม่ (Non-degree) Machine learning decision support for business problem มหาวิทยาลัยหอการค้าไทย

## Read full : 

Contributors :
- [@tussanakorn](https://github.com/tussanakorn)
- [@Trirat2543](https://github.com/Trirat2543)
- Chinnapat

### Project objectives
1. เพื่อออกแบบระบบที่สามารถคำนวณเบี้ยประกันที่เหมาะสมให้แก่ลูกค้าในแต่ละคนได้ 
2. เพื่อระบุปัจจัยที่ส่งผลต่อการคำนวณเบี้ยประกันของลูกค้าในบริษัท
3. เพื่อวิเคราะห์ข้อมูล และหาความสัมพันธ์ของชุดข้อมูล จนสามารถนำไปสู่การวางแผนแนวทางบริษัทในอนาคตได้

### Machine Learning Project LifeCycle  
credit : Code The Brain

![uWSkQS.png](https://sv1.picz.in.th/images/2021/10/06/uWSkQS.png)

Data from Kaggle >> https://www.kaggle.com/tejashvi14/medical-insurance-premium-prediction
Medical Insurance Premium Prediction : เป็นข้อมูลลูกค้าจำนวน 1000 รายจากบริษัทประกันภัยแห่งหนึ่ง 

### Review Result From KNIME Program

| Algorithms            | R-Squared         | Mean absolute error    | Mean squred error          |
| --------------------- | ------------------|----------------------- | -------------------------- |
|Gradient Boosted Trees (Regression) algorithms| 0.803 | 1,073.921   |7,067,584.475               |
|Linear Regression      | 0.66              | 2,882.87               | 14,923,033.855             |
|Random Forest learner (Regression) algorithms| 0.781  | 1,662.3     | 7,429,765.088              |
|K-Means clustering & linear regression  algorithms| 0.916 | 1,241.967 | 2,837,020.905            |

Link Digital Dashboard : https://app.powerbi.com/view?r=eyJrIjoiMzY0NDU2NjEtNjE3OS00ZmZhLWIwNzAtMWU1YzViYTk2ZWM1IiwidCI6IjZmNDQzMmRjLTIwZDItNDQxZC1iMWRiLWFjMzM4MGJhNjMzZCIsImMiOjEwfQ%3D%3D&pageName=ReportSection

[![uWVf8Z.png](https://sv1.picz.in.th/images/2021/10/06/uWVf8Z.png)](https://www.picz.in.th/image/uWVf8Z)
[![uWVBUu.png](https://sv1.picz.in.th/images/2021/10/06/uWVBUu.png)](https://www.picz.in.th/image/uWVBUu)

หลังจากสร้างโมเดลแล้ว เราก็นำโมเดลไป deploy แล้วนำมาต่อแชทบอท เพื่อใช้ในการ Predictive

### Chatbot 
[![uWVDH9.png](https://sv1.picz.in.th/images/2021/10/06/uWVDH9.png)](https://www.picz.in.th/image/uWVDH9)
[![uWVoqD.md.png](https://sv1.picz.in.th/images/2021/10/06/uWVoqD.md.png)](https://www.picz.in.th/image/uWVoqD)
[![uWVP7J.png](https://sv1.picz.in.th/images/2021/10/06/uWVP7J.png)](https://www.picz.in.th/image/uWVP7J)

### แผนผังโครงสร้าง Chatbot : Mr.healthy
[![uWVsgb.md.png](https://sv1.picz.in.th/images/2021/10/06/uWVsgb.md.png)](https://www.picz.in.th/image/uWVsgb)
