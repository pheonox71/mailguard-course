const STORAGE_KEY = 'mailguard-course-progress-v1'

export function loadProgress() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    if (!raw) {
      return { completedModules: {}, completedTopics: {}, lastModuleId: null, lastTopicId: null }
    }
    const parsed = JSON.parse(raw)
    return {
      completedModules: parsed.completedModules || {},
      completedTopics: parsed.completedTopics || {},
      lastModuleId: parsed.lastModuleId || null,
      lastTopicId: parsed.lastTopicId || null,
    }
  } catch {
    return { completedModules: {}, completedTopics: {}, lastModuleId: null, lastTopicId: null }
  }
}

export function saveProgress(state) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state))
}

export function resetProgress() {
  localStorage.removeItem(STORAGE_KEY)
}

export function markModuleVisited(moduleId, topicId = null) {
  const state = loadProgress()
  state.lastModuleId = moduleId
  if (topicId) state.lastTopicId = topicId
  saveProgress(state)
  return state
}

export function setModuleComplete(moduleId, complete) {
  const state = loadProgress()
  if (complete) state.completedModules[moduleId] = true
  else delete state.completedModules[moduleId]
  saveProgress(state)
  return state
}

export function setTopicComplete(moduleId, topicId, complete) {
  const state = loadProgress()
  const key = `${moduleId}::${topicId}`
  if (complete) state.completedTopics[key] = true
  else delete state.completedTopics[key]
  saveProgress(state)
  return state
}

export function isModuleComplete(state, moduleId) {
  return Boolean(state.completedModules[moduleId])
}

export function isTopicComplete(state, moduleId, topicId) {
  return Boolean(state.completedTopics[`${moduleId}::${topicId}`])
}

export function resumeTarget(modules) {
  const state = loadProgress()
  if (state.lastModuleId && modules.some((m) => m.id === state.lastModuleId)) {
    return { moduleId: state.lastModuleId, topicId: state.lastTopicId }
  }
  const firstIncomplete = modules.find((m) => !state.completedModules[m.id])
  if (firstIncomplete) return { moduleId: firstIncomplete.id, topicId: null }
  return { moduleId: modules[0]?.id || '00-setup', topicId: null }
}

export function resumeHref(modules) {
  const { moduleId, topicId } = resumeTarget(modules)
  const base = `module.html?id=${encodeURIComponent(moduleId)}`
  return topicId ? `${base}#topic-${encodeURIComponent(topicId)}` : base
}

export function resumeLabel(modules) {
  const state = loadProgress()
  const { moduleId } = resumeTarget(modules)
  const mod = modules.find((m) => m.id === moduleId)
  if (!mod) return 'Start Module 00'
  if (!state.lastModuleId && !Object.keys(state.completedModules).length) {
    return `Start Module ${mod.number}`
  }
  return `Continue Module ${mod.number}`
}
