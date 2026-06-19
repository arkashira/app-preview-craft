# TECH_SPEC.md: app-preview-craft

## 1. Overview

app-preview-craft is a cloud-based SaaS platform designed to empower indie iOS developers to create professional App Store preview videos without requiring video editing expertise. The platform provides template-based workflows, AI-assisted editing features, and seamless integration with iOS app assets to streamline the video creation process.

## 2. Architecture Overview

### 2.1 High-Level Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Client    │    │   Mobile Client │    │   Admin Portal  │
│   (React)       │    │   (iOS/Android) │    │   (React)       │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────┬───────────┴──────────┬─────────────┘
                     │                      │
            ┌────────▼──────────┐  ┌───────▼────────┐
            │   API Gateway     │  │   Auth Service │
            │   (Kong)          │  │   (OAuth 2.0)  │
            └────────┬──────────┘  └────────────────┘
                     │
          ┌─────────▼──────────┐
          │   Application      │
          │   Backend          │
          │   (Node.js/Express)│
          └─────────┬──────────┘
                    │
     ┌──────────────┼──────────────┐
     │              │              │
┌────▼────┐ ┌──────▼──────┐ ┌────▼────┐
│Template │ │  Media      │ │ Video   │
│Service  │ │ Processing  │ │ Service │
│(PostgreSQL)│ │(FFmpeg/Cloud)│ │(S3)     │
└─────────┘ └─────────────┘ └─────────┘
```

### 2.2 System Components

#### 2.2.1 Frontend
- **Web Client**: React-based interface for desktop users
- **Mobile Client**: iOS/Android companion app for asset management
- **Admin Portal**: For template and content management

#### 2.2.2 Backend Services
- **API Gateway**: Routes requests and manages rate limiting
- **Auth Service**: Handles user authentication and authorization
- **Application Backend**: Core business logic and API endpoints
- **Template Service**: Manages video templates and customization options
- **Media Processing Service**: Handles video rendering and processing
- **Video Service**: Manages video storage and delivery

## 3. Data Model

### 3.1 Core Entities

#### User
```typescript
interface User {
  id: string;
  email: string;
  username: string;
  plan: 'free' | 'pro' | 'enterprise';
  createdAt: Date;
  lastLoginAt: Date;
  preferences: {
    theme: 'light' | 'dark';
    defaultResolution: '720p' | '1080p' | '4k';
    autoSave: boolean;
  };
}
```

#### Project
```typescript
interface Project {
  id: string;
  userId: string;
  name: string;
  description: string;
  status: 'draft' | 'processing' | 'completed' | 'published';
  createdAt: Date;
  updatedAt: Date;
  templateId: string;
  assets: MediaAsset[];
  timeline: TimelineItem[];
  renderSettings: {
    resolution: string;
    fps: number;
    format: 'mp4' | 'mov';
    quality: 'low' | 'medium' | 'high';
  };
}
```

#### Template
```typescript
interface Template {
  id: string;
  name: string;
  description: string;
  category: 'app-showcase' | 'feature-highlight' | 'tutorial' | 'testimonial';
  thumbnail
