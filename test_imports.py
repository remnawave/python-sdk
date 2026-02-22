#!/usr/bin/env python3
"""Quick test to verify all new imports work"""

try:
    from remnawave.models import (
        ReorderConfigProfilesRequestDto,
        ReorderSubscriptionTemplatesRequestDto,
        ReorderInternalSquadsRequestDto,
        ReorderExternalSquadsRequestDto,
        GetSubpageConfigByShortUuidResponseDto,
    )
    print("✅ Все новые модели успешно импортируются!")
    print("   - ReorderConfigProfilesRequestDto")
    print("   - ReorderSubscriptionTemplatesRequestDto")
    print("   - ReorderInternalSquadsRequestDto")
    print("   - ReorderExternalSquadsRequestDto")
    print("   - GetSubpageConfigByShortUuidResponseDto")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    exit(1)
