/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   handle_p.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vchiling <vchiling@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/16 17:53:47 by vchiling          #+#    #+#             */
/*   Updated: 2026/03/16 18:12:30 by vchiling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	handle_p(va_list args)
{
	unsigned long	*ptr;
	char			*sptr;

	ptr = va_arg(args, unsigned long *);
	sptr = ft_ultoa_base(ptr, BASE_16);
	ft_putstr("0x");
	ft_putstr(sptr);
	return (ft_strlen(sptr) + 2);
}
