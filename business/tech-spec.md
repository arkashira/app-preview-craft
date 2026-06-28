```markdown
# Tech Spec: app-preview-craft

## Stack
- **Language**: TypeScript (Node.js runtime)
- **Framework**: Express.js (REST API) + React.js (frontend)
- **Runtime**: Node.js v18.x LTS
- **Build Tool**: Vite + Webpack
- **Testing**: Jest + Supertest
- **Deployment**: Dockerized microservice

## Hosting
- **Primary Platform**: AWS (EC2 + S3 + Lambda)
- **Free Tier First**: Use AWS Free Tier for initial MVP (till 1 year or $100/month cap)
- **CDN**: CloudFront for static assets
- **Database**: PostgreSQL (RDS) - managed DB instance
- **Storage**: S3 bucket for video assets and templates
- **Monitoring**: AWS CloudWatch + X-Ray

## Data Model
### Tables/Collections
1. **Users**
   - `id` (UUID)
   - `email` (string)
   - `name` (string)
   - `created_at` (timestamp)
   - `updated_at` (timestamp)

2. **Projects**
   - `id` (UUID)
   - `user_id` (UUID, FK to Users)
   - `title` (string)
   - `description` (text)
   - `template_id` (UUID, optional)
   - `status` (enum: draft, published)
   - `created_at` (timestamp)
   - `updated_at` (timestamp)

3. **Templates**
   - `id` (UUID)
   - `name` (string)
   - `description` (text)
   - `json_config` (JSONB)
   - `is_public` (boolean)
   - `created_by` (UUID, FK to Users)
   - `created_at` (timestamp)
   - `updated_at` (timestamp)

4. **Videos**
   - `id` (UUID)
   - `project_id` (UUID, FK to Projects)
   - `video_url` (string)
   - `thumbnail_url` (string)
   - `duration_seconds` (integer)
   - `status` (enum: processing, ready, failed)
   - `created_at` (timestamp)
   - `updated_at` (timestamp)

5. **Sessions**
   - `id` (UUID)
   - `user_id` (UUID, FK to Users)
   - `token` (string)
   - `expires_at` (timestamp)
   - `created_at` (timestamp)

## API Surface
1. `POST /api/auth/register`
   - Purpose: Register new user
2. `POST /api/auth/login`
   - Purpose: Authenticate user and return session token
3. `GET /api/projects`
   - Purpose: List user's projects
4. `POST /api/projects`
   - Purpose: Create new project
5. `GET /api/projects/{id}`
   - Purpose: Get project details
6. `PUT /api/projects/{id}`
   - Purpose: Update project metadata
7. `DELETE /api/projects/{id}`
   - Purpose: Delete project
8. `POST /api/videos/generate`
   - Purpose: Trigger video generation from project
9. `GET /api/templates`
   - Purpose: List available templates
10. `GET /api/videos/{id}/download`
    - Purpose: Download generated video file

## Security Model
- **Authentication**: JWT tokens via HTTPS-only cookies
- **Authorization**: Role-based access control (RBAC) with scopes
- **Secrets Management**: AWS Secrets Manager for API keys, database credentials
- **IAM**: AWS IAM roles for service permissions (S3 read/write, Lambda execution)
- **Data Encryption**: TLS 1.3 in transit, AES-256 in rest (S3 & RDS)
- **Rate Limiting**: IP-based rate limiting using Redis

## Observability
- **Logs**: Winston logger with structured JSON output to CloudWatch
- **Metrics**: Prometheus metrics exposed via `/metrics` endpoint
- **Traces**: OpenTelemetry with AWS X-Ray integration
- **Alerting**: Slack alerts for critical errors and performance degradation
- **Dashboard**: Grafana dashboards for system health monitoring

## Build/CI
- **Build System**: GitHub Actions workflows
- **CI Pipeline**: 
  - Run unit tests (`npm test`)
  - Lint code (`eslint`)
  - Build frontend (`npm run build`)
  - Run integration tests (`npm run test:integration`)
- **CD Pipeline**:
  - Deploy to staging on PR merge
  - Deploy to production on tag push
- **Dockerization**: Multi-stage Dockerfile for both frontend and backend services
- **Versioning**: Semantic versioning (SemVer) with automated changelog generation
```