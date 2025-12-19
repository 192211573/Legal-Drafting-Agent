# 🚀 Quick Start Guide - AI Legal Document Assistant

## ✅ What You Have Now

Your complete AI-powered legal document system with:
- ✓ Backend API running on http://localhost:8000
- ✓ Frontend app running on http://localhost:5173
- ✓ Custom AI model training capabilities
- ✓ Document analysis and drafting features

---

## 📋 Step-by-Step Usage Guide

### **Step 1: Register & Login** 👤

1. Open your browser: http://localhost:5173
2. Click "Register" or go to http://localhost:5173/register
3. Fill in your details:
   - Name: Your Name
   - Email: your@email.com
   - Password: (your password)
   - Role: User/Admin
4. Click "Register"
5. You'll be automatically logged in!

---

### **Step 2: Upload Training Documents** 📄

1. After login, go to **"Upload Document"** page
2. Click "Choose File" or drag & drop
3. Upload at least **2-3 legal documents** (contracts, agreements, etc.)
   - Supported formats: .txt, .pdf, .doc, .docx
   - Examples: Service agreements, NDAs, employment contracts
4. Click "Upload"
5. Repeat for multiple documents

**💡 Tip**: The more documents you upload, the better your AI model will learn!

---

### **Step 3: Train Your AI Model** 🧠

1. Go to **"Model Training"** page: http://localhost:5173/model-training
2. You'll see all your uploaded documents
3. **Select at least 2 documents** by checking the boxes
4. Click **"Train Model"** button
5. Wait for training to complete (usually 30-60 seconds)
6. You'll see: "Training completed! X documents processed"

**What happens during training:**
- AI extracts legal clauses and patterns
- Learns document structure and terminology
- Creates similarity embeddings
- Identifies common clause types

---

### **Step 4: Analyze Documents** 🔍

1. Go to **"Agent Selection"** page
2. Choose **"Risk Detection"** or **"Clause Extraction"**
3. Select a document to analyze
4. Click "Analyze"
5. View results:
   - Missing clauses
   - Risk assessment
   - Similar documents
   - Recommendations

---

### **Step 5: Generate Document Drafts** ✍️

1. Go to **"Drafting Agent"** page
2. Select a source document (optional)
3. Fill in parameters:
   - Document type (Service Agreement, NDA, etc.)
   - Party names
   - Jurisdiction
   - Required clauses
4. Click **"Generate Draft"**
5. Review the AI-generated document
6. Copy and customize as needed

---

## 🎯 **Key Features to Try**

### **1. Document Analysis**
- Upload a contract
- Use "Risk Detection" agent
- See what clauses are missing
- Get recommendations

### **2. Smart Drafting**
- Train on your documents
- Generate new contracts
- AI uses your document style
- Includes learned clauses

### **3. Similarity Search**
- Upload a new document
- AI finds similar documents
- Compare clauses and terms
- Learn from past documents

### **4. Dashboard Analytics**
- View document statistics
- See processing history
- Track agent usage
- Monitor model performance

---

## 🛠 **API Endpoints You Can Use**

### **Test with curl or Postman:**

```bash
# 1. Register User
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@example.com","password":"pass123","role":"User"}'

# 2. Login
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john@example.com&password=pass123"

# 3. Upload Document (save token from login)
curl -X POST http://localhost:8000/api/documents/upload \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@contract.pdf"

# 4. Start Training
curl -X POST http://localhost:8000/api/training/start \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"document_ids":[1,2,3],"model_name":"my_model"}'

# 5. Analyze Document
curl -X POST http://localhost:8000/api/training/analyze-document/1 \
  -H "Authorization: Bearer YOUR_TOKEN"

# 6. Generate Draft
curl -X POST http://localhost:8000/api/training/generate-draft \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"parameters":{"document_type":"service_agreement","party1":"Company A","party2":"Company B"}}'
```

---

## 📊 **What Each Agent Does**

### **Clause Extraction Agent**
- Extracts key clauses from documents
- Identifies clause types (termination, liability, etc.)
- Shows clause locations
- Provides confidence scores

### **Risk Detection Agent**
- Identifies potential legal risks
- Flags missing important clauses
- Assesses compliance issues
- Provides risk scores and recommendations

### **Drafting Agent**
- Generates new document content
- Uses learned patterns from training
- Creates contextual clauses
- Provides improvement suggestions

### **Summary Agent**
- Creates executive summaries
- Extracts key points
- Identifies parties and terms
- Provides document overview

---

## 🎓 **Best Practices**

1. **Training Data**: Upload 5-10 similar documents for best results
2. **Document Quality**: Use well-formatted legal documents
3. **Regular Updates**: Retrain model when adding new documents
4. **Review Outputs**: Always review AI-generated content
5. **Iterate**: The more you use it, the better it gets!

---

## 🐛 **Troubleshooting**

### **Backend not responding?**
```bash
cd backend
python run.py
```

### **Frontend not loading?**
```bash
npm install
npm run dev
```

### **CORS errors?**
- Backend already configured for localhost:5173
- Check both servers are running

### **Training fails?**
- Ensure at least 2 documents uploaded
- Check documents have substantial content (>100 words)
- View backend logs for errors

---

## 📚 **Next Level Features**

Once comfortable with basics, try:

1. **Batch Processing**: Analyze multiple documents at once
2. **Custom Templates**: Create document templates
3. **API Integration**: Build custom workflows
4. **Model Fine-tuning**: Train on specific document types
5. **Export Features**: Download analysis reports

---

## 🎉 **You're Ready!**

Your AI legal document assistant is fully operational. Start by:
1. ✅ Register an account
2. ✅ Upload 2-3 documents
3. ✅ Train your model
4. ✅ Analyze a document
5. ✅ Generate your first draft

**Need help?** Check the API docs at http://localhost:8000/docs

Happy drafting! 🚀