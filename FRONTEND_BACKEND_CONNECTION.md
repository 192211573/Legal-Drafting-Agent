# 🔗 Frontend-Backend Connection Guide

## ✅ **What We've Connected:**

### **Backend APIs Available:**
- ✅ Authentication (`/api/auth/*`)
- ✅ Document Management (`/api/documents/*`)
- ✅ AI Agents (`/api/agents/*`)
- ✅ Enhanced Drafting (`/api/drafting/*`)
- ✅ Model Training (`/api/training/*`)
- ✅ Analytics (`/api/analytics/*`)
- ✅ Notifications (`/api/notifications/*`)

### **Frontend Pages Connected:**
- ✅ Login/Register → Backend Auth
- ✅ Document Upload → Backend Storage
- ✅ Model Training → Backend AI Training
- ✅ Enhanced Drafting → Backend Legal Templates
- ✅ Integration Test → Connection Monitoring

---

## 🚀 **How to Test the Connection:**

### **Step 1: Start Both Servers**
```bash
# Terminal 1 - Backend
cd backend
python run.py

# Terminal 2 - Frontend  
npm run dev
```

### **Step 2: Test Connection**
1. Open: http://localhost:5173
2. Register a new account
3. Go to: http://localhost:5173/integration-test
4. Check all connection tests pass ✅

### **Step 3: Test Enhanced Drafting**
1. Go to: http://localhost:5173/enhanced-drafting
2. Select a document template
3. Fill in party details
4. Generate a legal document
5. Check quality score

---

## 📋 **Available Features:**

### **1. Enhanced Legal Drafting**
- **URL:** `/enhanced-drafting`
- **Features:**
  - 8 Professional legal templates
  - AI-powered customization
  - Quality scoring system
  - Legal compliance checking
  - Real-time suggestions

### **2. Model Training**
- **URL:** `/model-training`
- **Features:**
  - Upload legal documents
  - Train custom AI models
  - Document similarity analysis
  - Pattern recognition

### **3. Integration Testing**
- **URL:** `/integration-test`
- **Features:**
  - Connection status monitoring
  - API endpoint testing
  - CORS verification
  - Health checks

---

## 🛠 **API Endpoints:**

### **Enhanced Drafting API:**
```
POST /api/drafting/draft-document
GET  /api/drafting/templates
GET  /api/drafting/template/{type}
POST /api/drafting/quality-check
GET  /api/drafting/ai-models
POST /api/drafting/customize-template
GET  /api/drafting/drafting-history
```

### **Training API:**
```
POST /api/training/start
GET  /api/training/status
POST /api/training/analyze-document/{id}
POST /api/training/generate-draft
GET  /api/training/model-info
```

### **Authentication API:**
```
POST /api/auth/register
POST /api/auth/login
GET  /api/auth/me
```

---

## 🔧 **Configuration:**

### **Backend Configuration:**
- **Port:** 8000
- **Database:** MySQL (XAMPP)
- **CORS:** Enabled for localhost:5173
- **API Docs:** http://localhost:8000/docs

### **Frontend Configuration:**
- **Port:** 5173 (or next available)
- **API Base:** http://localhost:8000/api
- **Auto-reconnection:** Every 30 seconds

---

## 🎯 **Testing Checklist:**

### **✅ Connection Tests:**
- [ ] Backend starts without errors
- [ ] Frontend loads successfully
- [ ] Health check returns 200 OK
- [ ] API documentation accessible
- [ ] CORS headers present

### **✅ Authentication Tests:**
- [ ] User registration works
- [ ] User login works
- [ ] Protected routes require auth
- [ ] JWT tokens generated

### **✅ Drafting Tests:**
- [ ] Templates load successfully
- [ ] Document generation works
- [ ] Quality checking functions
- [ ] AI models respond

### **✅ Integration Tests:**
- [ ] All API calls succeed
- [ ] Error handling works
- [ ] Loading states display
- [ ] Success messages show

---

## 🐛 **Troubleshooting:**

### **Backend Not Starting:**
```bash
cd backend
pip install -r requirements.txt
python run.py
```

### **Frontend Not Loading:**
```bash
npm install
npm run dev
```

### **Connection Errors:**
1. Check both servers are running
2. Verify ports (8000 for backend, 5173+ for frontend)
3. Check CORS configuration
4. Test with integration test page

### **Database Errors:**
1. Start XAMPP
2. Create database: `deeplex_db`
3. Update connection string in `.env`

---

## 📚 **Next Steps:**

1. **Test the connection:** Visit `/integration-test`
2. **Try drafting:** Visit `/enhanced-drafting`
3. **Train a model:** Visit `/model-training`
4. **Check API docs:** Visit `http://localhost:8000/docs`

Your frontend and backend are now fully connected! 🎉