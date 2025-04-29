# 2025-04-29 - reports/langchain Project Daily Report

# LangChain Progress Report (2025-04-29)

## Key Open Issues

### Critical Functionality
- **Import Errors**: `AsyncCallbackManagerForLLMRun` import failure in `langchain_azure_ai` (#31061)
- **Security**: Remote email injection vulnerability (#30833)
- **Compatibility**: 
  - Chroma server incompatibility (#31047)
  - OpenAI SDK 1.0+ compatibility break (#30933)
  - Deepseek version conflicts (#30916)

### Core System Issues
- **Tool Calling**: 
  - Invalid dictionary argument handling (#30910)
  - Schema handling with recursive tools (#30797)
  - Bedrock/Mistral tool invocation failures (#30978)
- **Streaming**: 
  - GPT-4o model streaming errors (#30786)
  - Anthropic token callback issues (#30703)

### Database/Vector Store Problems
- PostgreSQL schema handling (#30976)
- Azure CosmosDB key errors (#30844, #30801)
- Pinecone value errors (#30715)

### Documentation Gaps
- ChatOpenAI token limits clarification (#31024)
- Google tools documentation (#30813)
- Vectorstore ID handling (#30622)

## Notable Pull Requests

### Core Improvements
- ✅ Union type support for OpenAI structured output (#30971)
- ⚠️ Community module migration to separate repo (#31060)
- 🛠️ Pydantic model cleanup (#30799)

### Documentation Updates
- Pinecone sparse vectorstore example (#31066)
- Astra DB notebook modernization (#30961)
- Chroma query filter syntax fixes (#31058)

### Bug Fixes
- Azure JSON schema streaming fix (#31062)
- PyMuPDF password handling (#31039)
- Anthropic system message handling (#30822)

### New Features
- PDF Router Parser proposal (#30847)
- ChatLLM7 integration (#30765)
- Recursive sitemap support for Gitbook (#30681)

## Commit Activity
- No commits recorded today

## Priority Areas
1. **Security**: Address email injection vulnerability
2. **Compatibility**: Resolve breaking changes with Chroma and OpenAI SDK
3. **Tool Reliability**: Improve tool calling consistency across providers
4. **Documentation**: Clarify key configuration parameters

Note: Several long-standing PRs (>30 days) remain open, particularly around PDF handling and core model improvements.