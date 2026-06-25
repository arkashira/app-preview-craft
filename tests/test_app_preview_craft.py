from app_preview_craft import (
    VideoAnalytics,
    get_app_store_conversion_rate_comparison,
    get_video_views_and_engagement_metrics,
    integrate_apple_developer_account,
    calculate_video_analytics
)
import pytest
import sys
sys.path.insert(0, '../src')

def test_get_app_store_conversion_rate_comparison():
    video_analytics = VideoAnalytics(
        conversion_rate_before=0.5,
        conversion_rate_after=0.7,
        video_views=100,
        engagement_metrics={"likes": 10, "comments": 5}
    )
    assert get_app_store_conversion_rate_comparison(video_analytics) == 0.2

def test_get_video_views_and_engagement_metrics():
    video_analytics = VideoAnalytics(
        conversion_rate_before=0.5,
        conversion_rate_after=0.7,
        video_views=100,
        engagement_metrics={"likes": 10, "comments": 5}
    )
    expected_result = {
        "video_views": 100,
        "engagement_metrics": {"likes": 10, "comments": 5}
    }
    assert get_video_views_and_engagement_metrics(video_analytics) == expected_result

def test_integrate_apple_developer_account():
    video_analytics = VideoAnalytics(
        conversion_rate_before=0.5,
        conversion_rate_after=0.7,
        video_views=100,
        engagement_metrics={"likes": 10, "comments": 5}
    )
    integrated_video_analytics = integrate_apple_developer_account(video_analytics)
    assert integrated_video_analytics.conversion_rate_after == 0.8

def test_calculate_video_analytics():
    video_analytics = calculate_video_analytics()
    assert video_analytics.conversion_rate_before == 0.5
    assert video_analytics.conversion_rate_after == 0.7
    assert video_analytics.video_views == 100
    assert video_analytics.engagement_metrics == {"likes": 10, "comments": 5}

def test_edge_case_zero_video_views():
    video_analytics = VideoAnalytics(
        conversion_rate_before=0.5,
        conversion_rate_after=0.7,
        video_views=0,
        engagement_metrics={"likes": 0, "comments": 0}
    )
    assert get_app_store_conversion_rate_comparison(video_analytics) == 0.2
    assert get_video_views_and_engagement_metrics(video_analytics) == {
        "video_views": 0,
        "engagement_metrics": {"likes": 0, "comments": 0}
    }
