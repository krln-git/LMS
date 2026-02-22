/* global gettext */
import React from 'react';
import { render, screen } from '@testing-library/react';
import { EnterpriseLearnerPortalModal } from './EnterpriseLearnerPortalModal';

// Mock dependencies
jest.mock('edx-ui-toolkit/js/utils/string-utils', () => ({
  interpolate: (text, context) => {
      let result = text;
      Object.keys(context).forEach(key => {
          result = result.replace(`{${key}}`, context[key]);
      });
      return result;
  },
}));

jest.mock('react-focus-lock', () => {
    const FocusLock = ({ children }) => <div>{children}</div>;
    FocusLock.AutoFocusInside = ({ children }) => <div>{children}</div>;
    return FocusLock;
});

describe('EnterpriseLearnerPortalModal', () => {
  const props = {
    enterpriseCustomerUUID: 'test-uuid',
    enterpriseCustomerName: 'Test Enterprise',
    enterpriseLearnerPortalBaseUrl: 'https://example.com',
    enterpriseCustomerSlug: 'test-slug',
  };

  beforeEach(() => {
    // Clear session storage
    window.sessionStorage.clear();
    // Mock analytics
    window.analytics = { track: jest.fn() };
    // Mock gettext if not present
    if (!global.gettext) {
        global.gettext = (text) => text;
    }
  });

  it('renders the modal with correct accessibility attributes', () => {
    render(<EnterpriseLearnerPortalModal {...props} />);

    // Check if dialog exists
    const dialog = screen.getByRole('dialog');
    expect(dialog).toBeInTheDocument();

    // These assertions are expected to fail initially
    expect(dialog).toHaveAttribute('aria-modal', 'true');
    expect(dialog).toHaveAttribute('aria-labelledby', `enterprise-modal-title-${props.enterpriseCustomerUUID}`);
    expect(dialog).toHaveAttribute('aria-describedby', `enterprise-modal-desc-${props.enterpriseCustomerUUID}`);

    // Check if title and description exist
    const title = screen.getByText(/You have access to the Test Enterprise dashboard/i);
    const description = screen.getByText(/To access the courses available to you through Test Enterprise/i);

    expect(title).toHaveAttribute('id', `enterprise-modal-title-${props.enterpriseCustomerUUID}`);
    expect(description).toHaveAttribute('id', `enterprise-modal-desc-${props.enterpriseCustomerUUID}`);
  });
});
