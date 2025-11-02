# RAGify

### 1. Start PostgreSQL via Docker
```bash
docker-compose up -d
```

### 2. Install Python dependencies
```bash
pipenv install
```

### 3. Test DB connection
```bash
python db_utils.py
```

### 4. Run LangChain Agent
```bash
python agent_lama.py
```

Ask questions like:
```
show all employees in Sales
who has the highest salary?
average salary by department
```
